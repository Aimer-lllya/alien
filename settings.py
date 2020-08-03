class Settings():
    """《外星人入侵》设置"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕尺寸
        self.screen_width = 1200
        self.screen_height = 600
        #背景颜色
        self.bg_color = (230,230,230)
        #飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #子弹
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1
