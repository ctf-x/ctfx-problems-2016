import random
import subprocess
import shlex
import sys

limit = 500
FLAG = "ctf(th3_cow_is_d4nk_m3m3ing)"

print "Do you know how the cow is feeling?"
print "Well now you can find out how all the cows feel; all {} of the cows in the herd!".format(limit)

cowsay_command = "cowsay {} {}"
feelings = {
	"": "just fine",
	"-d": "dead",
	"-e 'xx'": "playing dead",
	"-g": "greedy",
	"-p": "paranoid",
	"-s": "stoned",
	"-t": "sleepy",
	"-w": "excited",
}

for i in range(limit):
	option = random.choice(list(feelings.keys()))
	opt_name = feelings[option]

	cmd = cowsay_command.format(option, "MOOOOO")
	output = subprocess.check_output(cmd, shell=True)

	print output

	guess = raw_input("How is that cow feeling?\n> ")
	#print guess
	correct = opt_name.strip() == guess.strip()
	if not correct:
		print "Nope, that cow was {}. I guess you don't know your cows.".format(opt_name)
		sys.exit(0)

	print "Correct!"

print ""
print "Congrats. You know how the cows feel!"
print "The flag is {}".format(FLAG)
