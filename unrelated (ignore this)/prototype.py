import pygame
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None,10)
    blue = pygame.Color('royalblue')

    rendertext = font.render("Torch was added to your INVENTORY", blue, True)
    txt_surf = rendertext.copy()
    alpha_surf = pygame.Surface(txt_surf.get_size(), pygame.SRCALPHA)
    alpha = 255

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if alpha > 0:
            alpha = max(alpha-4, 0)
            txt_surf = rendertext.copy()
            rendertext.fill((255, 255, 255, alpha))
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
        screen.fill((30, 30, 30))
        screen.blit(txt_surf, (30, 60))
        pygame.display.flip()
        clock.tick(30)
        
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()