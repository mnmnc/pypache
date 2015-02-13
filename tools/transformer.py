
class Transformer:

	def adjust_item(self, local_string, i ):
		if len(local_string) < i:
			for j in range(i-len(local_string)):
				local_string = local_string + " "
		return local_string