import settings

def height_per(percent):
    return (settings.HEIGHT // 100) * percent

def width_per(percent):
    return (settings.WIDTH // 100) * percent