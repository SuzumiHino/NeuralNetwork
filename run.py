from main import main

try:
	main()
except TypeError:
	print("\nTypeError\n> Script is complete with TypeError")
finally:
	print("\nProgram completed")