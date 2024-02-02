# Extra things

## Default message
If you tried using our engine you may have encountered this message being printed to terminal:

```bash
Fusion Engine 5.0.0 (PyOpenGL 3.1.7, Pygame-ce 2.4.0, Python 3.11.7)
Welcome to Fusion Engine! Check out our website at https://fusion-engine.tech/
```

To disable this behavior, you just give the main class when initting this argument, set your "FUSION_HIDE_PROMPT" enviorment variable to "no" or anything else.
Or you can set the message variable to False:
```python
import fusionengine as fusion

fusion.message = False
```

## GL support
If you are using a OS that isn't officially being supported by Fusion and it still works, you can disable this warning:
```bash
Your platform could not be resolved. Defaulting to OpenGL as GL. Rever to the documentation to learn about how to remove this warning.
```
To disable this behavior, you just give the main class when initting this argument, set your "FUSION_HIDE_GL_PROMPT" enviorment variable to "no" or anything else.
