# coding:utf-8
# @Time    : 2024/12/19 13:31
# @Author  : Ryan
# @FileName: 模拟超市付款.py

# 用户输入商品价格
item_price = float(input("请输入商品的价格（元）："))

# 用户输入付款金额
paid_amount = float(input("请输入您的付款金额（元）："))

# 计算找零
change = paid_amount - item_price

# 提示用户找零金额
if change >= 0:
    print(f"您的找零是：{change:.2f}元。")
    # 提示是否需要找零
    give_change = input("需要找零吗？(yes/no)：")
    if give_change.lower() == 'yes':
        print("正在给您找零...")
    else:
        print("好的，不需要找零。")
else:
    print("付款金额不足，请支付更多。")