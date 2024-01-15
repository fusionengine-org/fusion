import pygame
from pygame.locals import *
from sdl2 import *


def main():
    pygame.init()
    pygame.display.set_caption("Mixed Rendering Example")

    width, height = 800, 600
    pygame_window = pygame.display.set_mode(
        (width, height), pygame.DOUBLEBUF | pygame.HWSURFACE
    )

    SDL_Init(SDL_INIT_VIDEO)
    sdl_window = SDL_CreateWindowFrom(pygame.display.get_wm_info()["window"])
    renderer = SDL_CreateRenderer(
        sdl_window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC
    )

    running = True
    clock = pygame.time.Clock()

    # Create a Pygame surface for rendering
    pygame_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    # Create a PySDL2 texture for rendering
    texture = SDL_CreateTexture(
        renderer, SDL_PIXELFORMAT_RGBA8888, SDL_TEXTUREACCESS_STREAMING, width, height
    )

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # PySDL2 rendering
        SDL_SetRenderTarget(renderer, texture)
        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0)
        SDL_RenderClear(renderer)
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 128)
        SDL_RenderDrawLine(renderer, 0, 0, width, height)
        SDL_RenderDrawLine(renderer, width, 0, 0, height)
        SDL_SetRenderTarget(renderer, None)

        # Update the Pygame surface with the PySDL2 texture pixels
        pixels, pitch = SDL_LockTexture(texture, None, None)
        pygame_surface = pygame.image.fromstring(pixels, (width, height), "RGBA", True)
        SDL_UnlockTexture(texture)

        # Draw the Pygame surface onto the Pygame window
        pygame_window.blit(pygame_surface, (0, 0))
        pygame.display.flip()

        clock.tick(60)

    SDL_DestroyTexture(texture)
    SDL_DestroyRenderer(renderer)
    SDL_DestroyWindow(sdl_window)
    SDL_Quit()
    pygame.quit()


if __name__ == "__main__":
    main()
