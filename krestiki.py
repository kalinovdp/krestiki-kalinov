
pole = ["1", "2", "3", "4", "5", "6", "7", "8","9"]
win_comb = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
X0 = ['X','O']


def draw_pole(pole):
	for i, c in enumerate(pole):
		if (i + 1)%3==0:
			print(f'{c}')
		else:
			print(f'{c} |', end=' ')


def get_winner(pole):
	for i in win_comb:
		if pole[i[0]] == pole[i[1]] == pole[i[2]]:
			return pole[i[0]]
	return False

def take_input(symb):
   end_turn = False
   while not end_turn:
      player_answer = input(f"Куда поставим {symb}? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(pole[player_answer-1]) not in X0):
            pole[player_answer-1] = symb
            end_turn = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def main(pole):
    counter = 0
    win = False
    while not win:
        draw_pole(pole)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = get_winner(pole)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_pole(pole)
main(pole)
