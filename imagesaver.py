 #imagesaver
import urllib.request, sys
from pprint import pprint as pp

def isurl(text):
  if "http://" in text or "https://" in text:
    return True

  else:
    return False


def parse_file(filename, names, links):
  text = ""

  with open(filename, mode='rt') as f:
    for line in f:
      text = line

      if text == '\n' or text is None:
        continue

      elif isurl(text):
        links.append(text.rstrip())
        continue

      else:
        names.append(text.strip())
        continue

  print("done parsing file")

  return names, links


def eval_lists(names=None, links=None, directory=None):
  if len(names) == len(links):
    print("names and links lists are same length!\nSaving images...\n")

    num_of_items  = len(names)
    success_count = 0
    failure_count = 0

    for i, link in enumerate(links):
      print("saving image", i+1, ", name =", names[i])

      try:
        save_image(link, names[i].strip(), directory)
        print("SUCCESS!" + "\n")
        success_count += 1

      except urllib.error.HTTPError as e:
        print("error accessing image '" + names[i].lstrip() + "' at:", link, " error =", e.code, "\n")
        failure_count += 1
        continue

  else:
    raise ValueError("Error, one or more 'name, link' pairs missing.\n"\
                     "Check input file and try again.\n\nScript terminated.")

  print("DONE!!!\n")
  links_grammar = "links"
  success_count_grammar = "were"
  only = ""

  if num_of_items == 1:
    links_grammar = "link"

  if success_count == 1:
    success_count_grammar = "was"
    only = "only"


  print("Out of {0} {1}, {2} {3} successfully downloaded and {4} failed.".format(num_of_items, links_grammar, success_count, success_count_grammar, failure_count))


def save_image(link, name, directory):
  full_path = directory + "\\" + name + ".jpg"
  local_filename, headers = urllib.request.urlretrieve(link, full_path)


def main():
  print("starting script....")
  names = []
  links = []

  input_file = input("paste the path to the text file containing image names and urls & press 'Enter.'")
  print()
  print("input file = ", input_file)
  directory  = input("now paste the path to the directory where you want to save the downloaded images & press 'Enter.'")
  print()
  print("directory = ", directory)

  print("parsing link file")
  names, links = parse_file(input_file, names, links)

  print("evaluating lists of names and links")
  eval_lists(names=names, links=links, directory=directory)
  print("\n\n----end of script----\n\n")


if __name__ == '__main__':
  main()
