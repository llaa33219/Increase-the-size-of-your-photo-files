from PIL import Image
import os

def create_large_png(image_path, output_path, data_size):
    with Image.open(image_path) as img:
        # 기본 이미지 저장
        img.save(output_path)

    # 무의미한 데이터 추가
    with open(output_path, 'ab') as f:
        f.write(os.urandom(data_size))

# 사용 예제
create_large_png('input.png', 'output.png', 10 * 1024 * 1024 * 1024)  # 10GB 무의미한 데이터 추가
