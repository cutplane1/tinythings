#include <windows.h>
#include <stdlib.h>
#include <time.h>
#include "libdrm.c"

#define width 800
#define height 600

RECT rect = {width/2 - 200, height/2 - 100, width/2 + 200, height/2 + 100};
COLORREF color = RGB(0, 0, 0);
int clicks = 0;
char buf[64];
HFONT hFont;

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    switch (msg)
    {
    case WM_CREATE:
        srand(time(NULL));
        hFont = CreateFont(
            36, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE,
            DEFAULT_CHARSET, OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS,
            DEFAULT_QUALITY, DEFAULT_PITCH | FF_SWISS, TEXT("Arial"));
        return 0;

    case WM_LBUTTONDOWN:
    {
        int x = LOWORD(lParam);
        int y = HIWORD(lParam);

        if (PtInRect(&rect, (POINT){x, y}))
        {
            clicks++;
            color = RGB(rand() % 256, rand() % 256, rand() % 256);
            InvalidateRect(hwnd, NULL, TRUE);
        }
        return 0;
    }

    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hwnd, &ps);
        SelectObject(hdc, hFont);

        HBRUSH brush = CreateSolidBrush(color);
        FillRect(hdc, &rect, brush);
        DeleteObject(brush);

        wsprintf(buf, "Clicks: %d", clicks);
        SetBkMode(hdc, TRANSPARENT);

        TextOut(hdc, 40, 40, buf, lstrlen(buf));

        EndPaint(hwnd, &ps);
        return 0;
    }

    case WM_SETCURSOR:
        SetCursor(LoadCursor(NULL, IDC_ARROW));
        return TRUE;

    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }

    return DefWindowProc(hwnd, msg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
                   LPSTR lpCmdLine, int nCmdShow)
{
    // i am too lazy to implement input window
    ask_for_license();
    HWND cmd = GetConsoleWindow();
    ShowWindow(cmd, SW_HIDE);
    const char CLASS_NAME[] = "RectangleclickingsimulatorClass";

    WNDCLASS wc = {0};
    wc.lpfnWndProc   = WndProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0,
        CLASS_NAME,
        "Rectangle clicking simulator 2013",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT, width, height,
        NULL,
        NULL,
        hInstance,
        NULL
    );


    ShowWindow(hwnd, nCmdShow);

    MSG msg = {0};
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return 0;
}
