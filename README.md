# abof-yolo11

Abnormal behavior of escalators (abof-yolo11)  使用 yolo11 框架监测扶梯乘客异常行为
## 目标

- 头手伸出扶梯外
- 逆行，奔跑，蹲下，弯腰，摔倒
- 大件行李，婴儿车
- 人流



## 详细

- 头手伸出扶梯外

自动识别扶梯并画一条线，使用姿态识别人的头手坐标，监测越线情况,[参考算法](https://www.bilibili.com/video/BV18E421P77Z/)

- 站立，跌倒，蹲下

人体纵向中心线与地面的倾斜角，倾斜角小于正负25度为跌倒，反之为站立或者坐的状态；同时结合人体宽高比，宽高比为 0.6  为站立，大于 5/3 为跌倒,[参考算法](https://www.bilibili.com/video/BV1Ps4y1w7DK/)


- 大件行李，婴儿车

使用物体识别, 首先将大件行李和人进行配对，比较行李和行人的检测狂，行李的长或者宽大于身长的1/3属于大件行李，小于1/3的可以带上扶梯,[参考算法](https://www.xjishu.com/zhuanli/55/202310461636.html)

- 人流

设置一个特定区域，有人进入就计数，[参考算法](https://www.youtube.com/watch?v=LH9xLtwLxQs)
