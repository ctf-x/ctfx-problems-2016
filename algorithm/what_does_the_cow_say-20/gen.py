import random
import subprocess
import shlex
import sys

limit = 1000
FLAG = "ctf(d4nk_gr33dy_cows)"

print "Do you know what the cow says?"
print "Well now you can find out... {} times over!".format(limit)

text_command = "./txt.sh"
cowsay_command = "cowsay -{} {}"
options = list("bdgpstwy")

for i in range(limit):
	text = subprocess.check_output(text_command)

	cmd = cowsay_command.format(random.choice(options), text)
	output = subprocess.check_output(cmd, shell=True)

	print output

	guess = raw_input("What did the cow say?\n> ")
	#print guess
	correct = text.strip() == guess.strip()
	if not correct:
		print "I guess you don't know what the cow says"
		sys.exit(0)

	print "Correct!"

print ""
print "Congrats. You know what the cow says!"
print "The flag is {}".format(FLAG)
