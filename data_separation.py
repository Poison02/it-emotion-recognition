# 将emotion和pixels像素数据分离
import pandas as pd

# 注意train.csv是在你电脑本地的相对或绝对路径地址
path = r'D:\git-test\facial-expression-recognition\dataset\train.csv'
# 读取数据
df = pd.read_csv(path)
# 提取emotion数据
df_y = df[['emotion']]
# 提取pixels数据
df_x = df[['pixels']]
# 将emotion写入emotion.csv
df_y.to_csv(r'D:\git-test\facial-expression-recognition\dataset\emotion.csv', index=False, header=False)
# 将pixels数据写入pixels.csv
df_x.to_csv(r'D:\git-test\facial-expression-recognition\dataset\pixels.csv', index=False, header=False)

# 处理fer2013数据集
# path = r'D:\git-test\facial-expression-recognition\dataset\fer2013.csv'
# df = pd.read_csv(path)
# df_y = df[['emotion']]
# df_x = df[['pixels']]
# df_y.to_csv(r'D:\git-test\facial-expression-recognition\dataset\fer_emotion.csv', index=False, header=False)
# df_x.to_csv(r'D:\git-test\facial-expression-recognition\dataset\fer_pixels.csv', index=False, header=False)