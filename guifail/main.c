#include <stdlib.h>
#include "fenster.h"
#include "fonts/5x5_font.h"

#define W 320
#define H 460

#define CHAR_WIDTH 6
#define CHAR_HEIGHT 8

void draw_char(struct fenster *f, char c, int x, int y, int scale, uint32_t color);
void draw_string(struct fenster *f, const char* str, int x, int y, int scale, uint32_t color);
void pixel_scale(struct fenster *f, int x, int y, int scale, uint32_t color);
void draw_rect_without_fill(struct fenster *f, int x, int y, int w, int h, uint32_t color);
void draw_rect_with_fill(struct fenster *f, int x, int y, int w, int h, uint32_t color);
void fenster_clear(struct fenster *f);
int btn(struct fenster *f, int x, int y, int w, int h, const char* ostr, const char* pstr, uint32_t color);

void pixel_scale(struct fenster *f, int x, int y, int scale, uint32_t color) {
    int x0 = x;
    int y0 = y;
    int x1 = x0 + scale;
    int y1 = y0 + scale;
    
    int clip_x0 = (x0 < 0) ? 0 : x0;
    int clip_y0 = (y0 < 0) ? 0 : y0;
    int clip_x1 = (x1 > f->width) ? f->width : x1;
    int clip_y1 = (y1 > f->height) ? f->height : y1;
    
    int w = clip_x1 - clip_x0;
    int h = clip_y1 - clip_y0;

    if (w > 0 && h > 0) {
        draw_rect_with_fill(f, clip_x0, clip_y0, w, h, color);
    }
}

void draw_char(struct fenster *f, char c, int x, int y, int scale, uint32_t color) {
    uint8_t i, j;

    c = c & 0x7F;
    if (c < ' ') {
        c = 0;
    } else {
        c -= ' ';
    }
    
    const uint8_t* chr = font[c];
    for (j = 0; j < CHAR_WIDTH; j++) {
        uint8_t col_data = chr[j];
        for (i = 0; i < CHAR_HEIGHT; i++) {
            if (col_data & (1 << i)) {
                int px = x + j * scale;
                int py = y + i * scale;
                pixel_scale(f, px, py, scale, color);
            }
        }
    }
}

void draw_string(struct fenster *f, const char* str, int x, int y, int scale, uint32_t color) {
    while (*str) {
        draw_char(f, *str++, x, y, scale, color);
        x += CHAR_WIDTH * scale;
    }
}

void draw_rect_without_fill(struct fenster *f, int x, int y, int w, int h, uint32_t color) {
    for (int i = x; i < x + w; i++) {
        fenster_pixel(f, i, y) = color;
        fenster_pixel(f, i, y + h - 1) = color;
    }
    for (int j = y; j < y + h; j++) {
        fenster_pixel(f, x, j) = color;
        fenster_pixel(f, x + w - 1, j) = color;
    }
}

void draw_rect_with_fill(struct fenster *f, int x, int y, int w, int h, uint32_t color) {
    for (int i = x; i < x + w; i++) {
        for (int j = y; j < y + h; j++) {
            fenster_pixel(f, i, j) = color;
        }
    }
}

void fenster_clear(struct fenster *f) {
    memset(f->buf, 0, (f->width * f->height) * sizeof(uint32_t));
}

int btn(struct fenster *f, int x, int y, int w, int h, const char* ostr, const char* pstr, uint32_t color) {
    if(f->mouse == 1 && f->x >= x && f->x < x + w && f->y >= y && f->y < y + h) {
        draw_rect_with_fill(f, x, y, w, h, color);
        draw_string(f, pstr, x+2, y+1, 2, 0x000000);
        return 1;
    } else {
        draw_rect_without_fill(f, x, y, w, h, color);
        draw_string(f, ostr, x+2, y+1, 2, color);
        return 0;
    }
}

int main() {
    uint32_t buf[W * H];
    struct fenster f = { .title = "hello", .width = W, .height = H, .buf = buf };
    fenster_open(&f);
    while (fenster_loop(&f) == 0) {
        fenster_clear(&f);
        if (btn(&f,10,10,120,60,"press!", "uwu", 0xffffff)) {
            draw_string(&f, "HELLO WORLD", 55, 180, 3, 0xf0f0f0);
        }
    }
    fenster_close(&f);
    return 0;
}
