import pygame
import pygame._sdl2 as pgsdl2
import sdl2
# Initialize SDL2 subsystems
sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

# Create a SDL2 window
sdl_window = sdl2.SDL_CreateWindow(
    b"Pygame with SDL2 Window",
    sdl2.SDL_WINDOWPOS_UNDEFINED,
    sdl2.SDL_WINDOWPOS_UNDEFINED,
    800,
    600,
    sdl2.SDL_WINDOW_SHOWN
)

# Initialize Pygame
pygame.init()

# Get the SDL window handle from Pygame
sdl_window_handle = pygame._sdl2.video.getSDLWindow(sdl_window)

# Bind the Pygame display surface to the SDL2 window
display = pygame.display.set_mode((800, 600), flags=pygame.SDL_WINDOW_OPENGL, hwnd=sdl_window_handle)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the display
    display.fill((0, 0, 0))
    
    # Draw a red rectangle using Pygame
    pygame.draw.rect(display, (255, 0, 0), (100, 100, 200, 150))

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()

# Destroy the SDL2 window
sdl2.SDL_DestroyWindow(sdl_window)
sdl2.SDL_Quit()

