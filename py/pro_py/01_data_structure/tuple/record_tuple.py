

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# passport는 리스트안의 튜플 한덩어리를 받는다.
# 그리고 문자열 포맷팅에서 % 뒤에 오는 값이 튜플이면 튜플의 요소가 각각의 %s에 대응된다.
for passport in sorted(traveler_ids):
  print('%s%s' % passport)


for country, _ in traveler_ids:
  print(country)