class SDXL_AspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "aspect_ratio": (["[1:1] 1024x1024", "[4:5] 896x1152", "[2:3] 832x1216", "[9:16] 768x1344", "[9:21] 640x1536", "[5:4] 1152x896", "[3:2] 1216x832", "[16:9] 1344x768", "[21:9] 1536x640"],),
            }
        }
    RETURN_TYPES = ("INT", "INT", "INT", "INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "2x width", "2x height", "4x width", "4x height")
    FUNCTION = "Aspect_Ratio"

    CATEGORY = "utils"

    def Aspect_Ratio(self, aspect_ratio):
        if aspect_ratio == "[1:1] 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "[4:5] 896x1152":
            width, height = 896, 1152
        elif aspect_ratio == "[2:3] 832x1216":
            width, height = 832, 1216
        elif aspect_ratio == "[9:16] 768x1344":
            width, height = 768, 1344
        elif aspect_ratio == "[9:21] 640x1536":
            width, height = 640, 1536
        elif aspect_ratio == "[5:4] 1152x896":
            width, height = 1152, 896
        elif aspect_ratio == "[3:2] 1216x832":
            width, height = 1216, 832
        elif aspect_ratio == "[16:9] 1344x768":
            width, height = 1344, 768
        elif aspect_ratio == "[21:9] 1536x640":
            width, height = 1536, 640

        width_x2 = width * 2
        height_x2 = height * 2
        width_x4 = width * 4
        height_x4 = height * 4

        print(width, height, width_x2, height_x2, width_x4, height_x4)
            
        return(width, height, width_x2, height_x2, width_x4, height_x4)


NODE_CLASS_MAPPINGS = {
    "SDXL_AspectRatio": SDXL_AspectRatio
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXL_AspectRatio": "SDXL Aspect Ratio Selector",
}
