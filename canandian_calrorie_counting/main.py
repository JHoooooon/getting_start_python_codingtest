"""
`Chip's Fast Food` 백화점에는 매우 심플한 메뉴가 있다
각 음식은 숫자를 입력하여 선택된다

Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger

Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink

Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order

Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert

식사의 총 칼로리를 계산하는 프로그램을 작성하라

- 입력

첫번째 라인은 burger 메뉴
두번째 라인은 side 메뉴
세번째 라인은 drink 메뉴
네번째 라인은 dessert 메뉴

각 메뉴마다 1 부터 4 까지 입력가능하며, 메뉴당 하나만 선택가능하다

- 출력

선택된 음식의 총 칼로리를 출력후 실행을 중지하라

sample input
2
1
3
4

sample output
Your total Calorie count is 649.
"""

# burger 메뉴
BURGER = int(input(
  """
  Here are the three burger choices:
  1 – Cheeseburger (461 Calories)
  2 – Fish Burger (431 Calories)
  3 – Veggie Burger (420 Calories)
  4 – no burger
  """
))

# side 메뉴
SIDE = int(input(
  """
  Here are the three side order choices:
  1 – Fries (100 Calories)
  2 – Baked Potato (57 Calories)
  3 – Chef Salad (70 Calories)
  4 – no side order
  """
))

# drink 메뉴
DRINK = int(input(
  """
  Here are the three drink choices:
  1 – Soft Drink (130 Calories)
  2 – Orange Juice (160 Calories)
  3 – Milk (118 Calories)
  4 – no drink
  """
))

# dessert 메뉴
DESSERT = int(input(
  """
  Here are the three dessert choices:
  1 – Apple Pie (167 Calories)
  2 – Sundae (266 Calories)
  3 – Fruit Cup (75 Calories)
  4 – no dessert
  """
))

def get_calorie(menuIdx: int, mealIdx: int):
  cal = [[461, 431, 420, 0], [100, 57, 40, 0], [130, 160, 118, 0], [167, 266, 75, 0]]
  return cal[menuIdx][mealIdx - 1];

total_cal = get_calorie(0, BURGER) + get_calorie(1, SIDE) + get_calorie(2, DRINK) + get_calorie(3, DESSERT)

print(f"Your total Calorie count is {total_cal}")



