#include <windows.h>
#include <stdio.h>

#define COBJMACROS
#include <initguid.h>
#include <shlobj.h>
#include <exdisp.h>
#include <shlguid.h>
#include <oleauto.h>
#include <shldisp.h>
#include <shlwapi.h>

#define MAX_WINDOWS 64

HWND windowses[MAX_WINDOWS];
size_t window_count = 0;

BOOL is_window_a_explorer(HWND hwnd)
{
    wchar_t class_name[256];
    GetClassNameW(hwnd, class_name, sizeof(class_name) / sizeof(wchar_t));
    return wcscmp(class_name, L"CabinetWClass") == 0 || wcscmp(class_name, L"ExploreWClass") == 0;
}

BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam)
{
    if (window_count >= MAX_WINDOWS)
    {
        return FALSE;
    }
    if (is_window_a_explorer(hwnd))
    {
        windowses[window_count++] = hwnd;
    }
    return TRUE;
}

int get_z_order(HWND hwnd)
{
    int z = 0;
    for (HWND top = GetTopWindow(NULL); top != NULL; top = GetNextWindow(top, GW_HWNDNEXT))
    {
        if (top == hwnd)
            return z;
        ++z;
    }
    return -1;
}

HWND last_active_explorer_window(void)
{
    EnumWindows(EnumWindowsProc, 0);

    int min_z = 0xB00B1E5;
    HWND last_hwnd = NULL;

    for (size_t i = 0; i < window_count; ++i)
    {
        int z = get_z_order(windowses[i]);
        if (z < min_z)
        {
            min_z = z;
            last_hwnd = windowses[i];
        }
    }

    return last_hwnd;
}

int main()
{
    HWND last = last_active_explorer_window();
    if (!last)
    {
        return 1;
    }

    CoInitialize(NULL);

    IShellWindows *pShellWindows = NULL;
    HRESULT hr = CoCreateInstance(
        &CLSID_ShellWindows,
        NULL,
        CLSCTX_ALL,
        &IID_IShellWindows,
        (void **)&pShellWindows);

    if (FAILED(hr))
    {
        CoUninitialize();
        return 1;
    }

    long count;
    pShellWindows->lpVtbl->get_Count(pShellWindows, &count);

    for (long i = 0; i < count; i++)
    {
        VARIANT vt;
        VariantInit(&vt);
        vt.vt = VT_I4;
        vt.lVal = i;

        BSTR url = NULL;
        HWND hwnd = NULL;
        IDispatch *pDisp = NULL;
        if (SUCCEEDED(pShellWindows->lpVtbl->Item(pShellWindows, vt, &pDisp)))
        {
            IWebBrowserApp *pBrowser;
            if (SUCCEEDED(pDisp->lpVtbl->QueryInterface(pDisp, &IID_IWebBrowserApp, (void **)&pBrowser)))
            {
                BSTR url = NULL;
                HWND hwnd = NULL;

                pBrowser->lpVtbl->get_LocationURL(pBrowser, &url);
                pBrowser->lpVtbl->get_HWND(pBrowser, (SHANDLE_PTR *)&hwnd);


if (hwnd == last && url) {
    // Пропускаем file:///
    const wchar_t* path_start = url;
    if (wcsncmp(url, L"file:///", 8) == 0)
        path_start += 8;

    // Печатаем прямо — русские буквы выводятся корректно
    wprintf(L"%ls\n", path_start);
}

                SysFreeString(url);
                pBrowser->lpVtbl->Release(pBrowser);
            }
            pDisp->lpVtbl->Release(pDisp);
        }
        VariantClear(&vt);
    }

    pShellWindows->lpVtbl->Release(pShellWindows);
    CoUninitialize();
    return 0;
}
