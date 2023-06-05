import sdl2

# Initialize SDL
sdl2.SDL_Init(sdl2.SDL_INIT_VIDEO)

# Create a window
window_width = 800
window_height = 600
window = sdl2.SDL_CreateWindow(b"Rectangle", sdl2.SDL_WINDOWPOS_UNDEFINED, sdl2.SDL_WINDOWPOS_UNDEFINED, window_width, window_height, sdl2.SDL_WINDOW_SHOWN)

# Create a renderer
renderer = sdl2.SDL_CreateRenderer(window, -1, sdl2.SDL_RENDERER_ACCELERATED)

# Set the drawing color
rectangle_color = sdl2.SDL_Color(255, 0, 0)  # Red color (adjust RGB values as needed)

# Clear the renderer
#sdl2.SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0)
sdl2.SDL_RenderClear(renderer)

# Set the color for drawing the rectangle
sdl2.SDL_SetRenderDrawColor(renderer, rectangle_color.r, rectangle_color.g, rectangle_color.b, rectangle_color.a)

# Create a rectangle
rectangle_width = 200
rectangle_height = 100
rectangle_x = (window_width - rectangle_width) // 2  # Center the rectangle horizontally
rectangle_y = (window_height - rectangle_height) // 2  # Center the rectangle vertically
rectangle = sdl2.SDL_Rect(rectangle_x, rectangle_y, rectangle_width, rectangle_height)

# Draw the rectangle
sdl2.SDL_RenderFillRect(renderer, rectangle)

# Update the renderer
sdl2.SDL_RenderPresent(renderer)

# Wait for the window to close
running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(event) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

# Clean up and quit
sdl2.SDL_DestroyRenderer(renderer)
sdl2.SDL_DestroyWindow(window)
sdl2.SDL_Quit()
