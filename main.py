import os
import random
import time

print("\033[35m", "\n\n\n\nThe Ultimate ToDo List Manager.", "\033[0m")
print("\033[31m", "<------------------------------->\n", "\033[0m")
print("\n\n\nLoading the ToDo App....\n")
print("please wait....")
time.sleep(5)
os.system("clear")

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
normal = "\033[0m"
some = "\033[35m"

user_todo_list = []


def xxx():
  while True:
    print(red, "sorry you do not have this event in your ToDo list\n", normal)
    print("try again\n\n")
    insert = input(
        "\n\n\n******* Enter what you want to remove from ToDO list --> ")
    print()
    if not user_todo_list:
      print(red, "you do not have any event in your ToDo list\n", normal)
      break
    elif insert in user_todo_list:
      user_todo_list.remove(insert)
      print(green, "\nSuccessfully removed", normal)
      break
    else:
      print(red, "\nsorry you do not have this event in your ToDo list\n",
            normal)
      print("try again")


def main_pro():

  while True:
    decide = input(
        "\n\n\nyou want to view, add, remove or edit the ToDo List? 🤔-------> "
    )
    # increment = increment + 1
    if decide == "view":
      num = 1
      for i in user_todo_list:
        print("\033[32m", num, i, "\033[0m")
        num = num + 1

      if not user_todo_list:
        print(
            "\033[34m",
            "\nyou do not got any event planned so far....please add one and try again",
            "\033[0m")

    elif decide == "add":
      insert = input(
          "\n\n\n ****** Enter what you want to add to your ToDo list --> ")
      if insert in user_todo_list:
        print(red, "\nYou already have this event in your ToDo list\n", normal)
        continue
      print()
      user_todo_list.append(insert)
      print(green, "\nSuccessfully added", normal)

    elif decide == "remove":
      while True:
        if not user_todo_list:
          print(
              red,
              "\nyou do not have any event in your ToDo list. First add one and try again\n",
              normal)
          break
        insert = input(
            "\n\n\n ******* Enter what you want to remove from ToDO list --> ")
        if insert not in user_todo_list:
          print(red, "\nsorry you do not have this event in your ToDo list\n",
                normal)
          print("try again")
          continue
        print()
        crosscheck = input(
            f"Are you sure you want to remove '{insert}' from your ToDo list? 🤔 (yes or no)-->"
        )
        if crosscheck == "yes":
          if insert in user_todo_list:
            user_todo_list.remove(insert)
            print(green, "\nSuccessfully romoved", normal)
            break
        elif crosscheck == "no":
          print(green, "\nProcess of removing was cancelled.", normal)
          break
        else:
          print(red, "\nyou can only input yes or no", normal)
          continue

    elif decide == "edit":
      if user_todo_list == []:
        print(
            some,
            "\nThere is no event in your ToDo list to edit. First add one and try again.",
            normal)
        continue
      insert = input(
          "\n\n\n ******* Enter what you want to edit from ToDO list --> ")
      print()
      if insert in user_todo_list:
        user_todo_list.remove(insert)
        # print(green, "\nSuccessfully removed", normal)
        # insert = input(
        #     "\n\n\n ******* Enter what you want to add to your ToDo list --> "
        # )
        print()
        what_to_add = input("what do you want to add? --> ")
        user_todo_list.append(what_to_add)
        print(green, "\nSuccessfully edited", normal)

      elif insert not in user_todo_list:
        xxx()
    else:
      print(
          red,
          "\nyou can only input add, view or remove (Lowercase). Please try AGAIN.\n",
          normal)
      continue

    while True:
      print(yellow, "\nSaving....", normal)
      time.sleep(5)
      os.system("clear")
      print("\033[35m", "\nThe Ultimate ToDo List Manager.", "\033[0m")
      print("\033[31m", "<------------------------------->\n", "\033[0m")

      print(
          red,
          "\n\n If some unexpected error occurs, please run the programe again.",
          normal)
      print(
          "<---------------------------------------------------------------------->\n"
      )
      done = input(
          "\n\n ****** done with the making of your ToDo? 🤔 (yes or no)----> ")
      if done == "yes":
        os.system("clear")
        print("\n\n\n\n\nSaving Your Data...\n\nPlease wait..")
        time.sleep(5)
        os.system("clear")
        print("\n\n\nhere's your final ToDo for today.\n\n")
        print()
        b = 1
        for i in user_todo_list:
          print(f"{some}{b}. {i}{normal}\n")
          b = b + 1
        print()
        print("All The Best For Today!!!! 👍👍")
        print(
            yellow,
            "\n\n-------------- Thanks for using ToDo list management-------------------\n\n",
            normal)

        exit()
      if done == "no":
        main_pro()
      else:
        print(red, "\nyou can only input yes or no", normal)
        continue


a = 1
while a == 1:
  print()
  print("\033[35m", "The Ultimate ToDo List Manager.", "\033[0m")
  print("\033[31m", "<------------------------------->\n", "\033[0m")
  print(
      red,
      "\n\n If some unexpected error occurs, please run the programe again.",
      normal)
  print(
      "<---------------------------------------------------------------------->\n"
  )

  a += 1
  main_pro()
