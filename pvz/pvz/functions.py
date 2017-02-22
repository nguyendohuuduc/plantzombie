def add_to_screen(obj, gameDisplay):
    gameDisplay.blit(obj.image, [obj.rect.x, obj.rect.y, obj.x_size, obj.y_size])
