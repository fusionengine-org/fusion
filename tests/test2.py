import sys
import sdl2
import sdl2.ext
import ctypes

# Initialize SDL
sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

# Create a window
window = sdl2.SDL_CreateWindow(b"Image Rendering", sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, 640, 480, sdl2.SDL_WINDOW_SHOWN)

# Create a renderer
renderer = sdl2.SDL_CreateRenderer(window, -1, 0)

# Load the image
image = sdl2.ext.load_image("test.png")

# Create a texture from the image
texture = sdl2.SDL_CreateTextureFromSurface(renderer, image)

# Clear the renderer
sdl2.SDL_RenderClear(renderer)

# Render the texture to the renderer
sdl2.SDL_RenderCopy(renderer, texture, None, None)

# Update the renderer
sdl2.SDL_RenderPresent(renderer)

# Main loop
running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

# Cleanup
sdl2.SDL_DestroyTexture(texture)
sdl2.SDL_FreeSurface(image)
sdl2.SDL_DestroyRenderer(renderer)
sdl2.SDL_DestroyWindow(window)
sdl2.SDL_Quit()
