#include <windows.h>

char syms[] = "Oo3)}D*";
char s[7] = "yum :";

int owo = 0;

void move_mouse()
{
    INPUT i = {0};
    i.type = INPUT_MOUSE;
    if (owo == 0) {
        i.mi.dx = 1;
        owo = 1;
    } else {
        i.mi.dx = -1;
        owo = 0;
    }
    i.mi.dy = 0;
    i.mi.dwFlags = MOUSEEVENTF_MOVE;
    SendInput(1, &i, sizeof(i));
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam)
{
    switch (msg)
    {
        case WM_CREATE:
        {
            SetTimer(hwnd, 1337, 30 * 1000, NULL);
            return 0;
        }

        case WM_TIMER:
            move_mouse();
        return 0;

        case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            HFONT hFont = CreateFontA(
                24, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE,
                DEFAULT_CHARSET, OUT_DEFAULT_PRECIS,
                CLIP_DEFAULT_PRECIS, CLEARTYPE_QUALITY,
                DEFAULT_PITCH | FF_DONTCARE,
                "MS Gothic"
            );
            HFONT hOld = (HFONT)SelectObject(hdc, hFont);

            RECT rc;
            GetClientRect(hwnd, &rc);
            DrawTextA(hdc, s, -1, &rc, DT_SINGLELINE | DT_CENTER | DT_VCENTER);

            SelectObject(hdc, hOld);
            DeleteObject(hFont);
            EndPaint(hwnd, &ps);
        }
    return 0;

    case WM_DESTROY:
        KillTimer(hwnd, 1337);
        PostQuitMessage(0);
        return 0;
    }

    return DefWindowProcA(hwnd, msg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    srand(time(NULL));
    s[5] = syms[rand()%7];
    s[6] = '\0';
    WNDCLASSA wc = {0};
    wc.lpfnWndProc   = WndProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = "CaffeinePillWindowClassOrSomething";
    wc.hCursor       = LoadCursor(NULL, IDC_ARROW);
    wc.hIcon         = (HICON) LoadImage(GetModuleHandle(NULL), "MY_ICON", IMAGE_ICON, 32, 32, 0);
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);

    RegisterClassA(&wc);

    HWND hwnd = CreateWindowExA(
        0,
        "CaffeinePillWindowClassOrSomething",
        "caffeine pill",
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU,
        CW_USEDEFAULT, CW_USEDEFAULT, 150, 100,
        NULL, NULL, hInstance, NULL
    );

    if (!hwnd) return 0;

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    MSG msg;
    while (GetMessageA(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessageA(&msg);
    }

    return (int)msg.wParam;
}
