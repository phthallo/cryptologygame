import pygame as pg
pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((640, 480))
font = pg.font.Font(None, 64)
blue = pg.Color('royalblue')
orig_surf = font.render('TORCH was added to your inventory', True, blue)
txt_surf = orig_surf.copy()
    # This surface is used to adjust the alpha of the txt_surf.
alpha_surf = pg.Surface(txt_surf.get_size(), pg.SRCALPHA)
alpha = 255  # The current alpha value of the surface.

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    orig_surf = font.render('NOTTORCH was added to your inventory', True, blue)
    txt_surf = orig_surf.copy()
    if alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
        alpha = max(alpha-4, 0)
        txt_surf = orig_surf.copy()  # Don't modify the original text surf.
            # Fill alpha_surf with this color to set its alpha value.
        alpha_surf.fill((255, 255, 255, alpha))
            # To make the text surface transparent, blit the transparent
            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
        txt_surf.blit(alpha_surf, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    screen.fill((30, 30, 30))
    screen.blit(txt_surf, (30, 60))
    pg.display.flip()
    clock.tick(30)

