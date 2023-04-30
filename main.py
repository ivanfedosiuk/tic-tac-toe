from kivy.app import App
from kivy.lang.builder import Builder



class MainApp(App):
	title = "Хрестики нулики"
	def build(self):
		return Builder.load_file('toe.kv')
		
	# Визначити чий зараз хід
	turn = "X"
	# Визначити перемога чи поразка
	winner = False
	
	# Вести запис перемог
	X_win = 0
	O_win = 0


	# Нічия
	def no_winner(self):
		if self.winner == False and \
		self.root.ids.btn1.disabled == True and \
		self.root.ids.btn2.disabled == True and \
		self.root.ids.btn3.disabled == True and \
		self.root.ids.btn4.disabled == True and \
		self.root.ids.btn5.disabled == True and \
		self.root.ids.btn6.disabled == True and \
		self.root.ids.btn7.disabled == True and \
		self.root.ids.btn8.disabled == True and \
		self.root.ids.btn9.disabled == True:
			self.root.ids.score.text = "Це Нічия!!"

	# Кінець гри
	def end_game(self, a,b,c):
		self.winner = True
		a.color = "red"
		b.color = "red"
		c.color = "red"

		# Вимкнути всі кнопки
		self.disable_all_buttons()

		# Поставити рахунок перемог
		self.root.ids.score.text = f"{a.text} Виграє!"

		# Логіка рахунку
		if a.text == "X":
			self.X_win = self.X_win + 1	
		else:
			self.O_win = self.O_win + 1

		self.root.ids.game.text = f"X Виграв: {self.X_win}  |  O Виграв: {self.O_win}"

	def disable_all_buttons(self):
		self.root.ids.btn1.disabled = True
		self.root.ids.btn2.disabled = True
		self.root.ids.btn3.disabled = True
		self.root.ids.btn4.disabled = True
		self.root.ids.btn5.disabled = True
		self.root.ids.btn6.disabled = True
		self.root.ids.btn7.disabled = True
		self.root.ids.btn8.disabled = True
		self.root.ids.btn9.disabled = True
    
    # типи перемог 
	def win(self):
		# Поперек
		if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
			self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

		if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
			self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

		if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
			self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)
		# Вниз
		if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
			self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

		if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
			self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

		if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
			self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

		# Діагональ
		if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
			self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

		if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
			self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

		self.no_winner()

	def presser(self, btn):
		if self.turn == 'X':
			btn.text = "X"
			btn.disabled = True
			self.root.ids.score.text = "O ходить!"
			self.turn = "O"
		else:
			btn.text = "O"
			btn.disabled = True
			self.root.ids.score.text = "X ходить!"
			self.turn = "X"

		self.win()

	def restart(self):
		# Визначити хто ходить після рестарту
		self.turn = "X"

		# Увімкнути кнопки
		self.root.ids.btn1.disabled = False
		self.root.ids.btn2.disabled = False
		self.root.ids.btn3.disabled = False
		self.root.ids.btn4.disabled = False
		self.root.ids.btn5.disabled = False
		self.root.ids.btn6.disabled = False
		self.root.ids.btn7.disabled = False
		self.root.ids.btn8.disabled = False
		self.root.ids.btn9.disabled = False

		# Зробити кнопки пустими
		self.root.ids.btn1.text = ""
		self.root.ids.btn2.text = ""
		self.root.ids.btn3.text = ""
		self.root.ids.btn4.text = ""
		self.root.ids.btn5.text = ""
		self.root.ids.btn6.text = ""
		self.root.ids.btn7.text = ""
		self.root.ids.btn8.text = ""
		self.root.ids.btn9.text = ""

		# відновити кольори
		self.root.ids.btn1.color = "grey"
		self.root.ids.btn2.color = "grey"
		self.root.ids.btn3.color = "grey"
		self.root.ids.btn4.color = "grey"
		self.root.ids.btn5.color = "grey"
		self.root.ids.btn6.color = "grey"
		self.root.ids.btn7.color = "grey"
		self.root.ids.btn8.color = "grey"
		self.root.ids.btn9.color = "grey"

		# Сказати хто ходить перший
		self.root.ids.score.text = "X ходить перший!"

		# Відновити значення переможця
		self.winner = False


MainApp().run()