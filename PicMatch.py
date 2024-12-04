from PIL import Image


def calculate_pixel_difference(image_path1, image_path2):
    # 打开两张图片
    image1 = Image.open(image_path1).convert('RGB')
    image2 = Image.open(image_path2).convert('RGB')

    # 确保两张图片的尺寸相同
    if image1.size != image2.size:
        raise ValueError("Images do not have the same size")

    # 计算像素差异
    difference = 0
    for x in range(image1.width):
        for y in range(image1.height):
            # 获取对应像素点的RGB值
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            # 计算RGB值之差的平方和
            diff = sum((p1 - p2) ** 2 for p1, p2 in zip(pixel1, pixel2))
            difference += diff
    max_possible_difference = 3 * (255 ** 2) * image1.width * image1.height
    similarity_score = 1 - (difference / max_possible_difference)
    return similarity_score
    # percent_score = "{:.2%}".format(similarity_score)
    # return percent_score


def determine(self,image_path1, image_path2):
    score1 = calculate_pixel_difference(image_path1, image_path2)
    score2 = int(score1 * 100)
    print(score2)
    if score2 < 60:
        print("测试失败")
        self.assertEqual(1, 2)
        #return False

    else:
        print("测试通过")


# 示例用法
"""
image_path1 = 'D:/bug/wjc_test/screen1.png'
image_path2 = 'D:/bug/wjc_test/screen2.png'

difference = calculate_pixel_difference(image_path1, image_path2)
print(f"Similarity Score: {difference}")
"""
