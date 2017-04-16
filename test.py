from visual import *

fps = 48

faces = {
            'r': (color.red, (1, 0, 0)),
            #'o': (color.orange, (-1, 0, 0)),
            #'y': (color.yellow, (0, 1, 0)),
            #'b': (color.blue, (0, -1, 0)),
            #'w': (color.white, (0, 0, 1)),
            #'g': (color.green, (0, 0, -1))
        }

stickers = []

for face_color, axis in faces.values():
    for x in (-0.5, 0.5):
        if x == -0.5:
            continue
        for y in (-0.5, 0.5):
            if x == -0.5:
                continue
            sticker = box(color=face_color, pos=(x, y, 1),
                    length = 0.98, height = 0.98, width = 0.05)
            cos_angle = dot((0, 0, 1), axis)
            pivot = (cross((0, 0, 1), axis) if cos_angle == 0 else (1, 0, 0))
            sticker.rotate(angle = acos(cos_angle), axis = pivot, origin = (0, 0, 0))
            stickers.append(sticker)

while True:
    key = scene.kb.getkey()
    if key.lower() in faces:
        face_color, axis= faces[key.lower()]
        angle = ((pi / 2) if key.isupper() else -pi / 2)
        for r in arange(0, angle, angle/fps):
            rate(fps)
            for sticker in stickers:
                if dot(sticker.pos, axis) >= 0.4:
                    sticker.rotate(angle = angle/fps, axis = axis, origin = (0, 0, 0))

