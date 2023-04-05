visual = ['rereading', 'colour-coding', 'watching videos', 'mindmaps', 'flashcards']
auditory = ['mneunomics', 'memorising using songs', 'videos', 'listening to podcasts']
reading/writing = ['rewriting notes', 'practising answering techniques']
kinesthetic = ['highlighting', 'underlining', 'watching visual simulations', 'hands-on experiments']

input_string = input('Enter the list of your current learning styles: ')
current_learning_style = input_string.split()
visual_score = 0
auditory_score = 0
reading/writing_score = 0
kinesthetic = 0
for i in range(len(current_learning_style)): 
  if current_learning_style[i] in visual: 
    visual_score_1 += 1
  if current_learning_style[i] in auditory: 
    auditory_score_1 += 1
  if current_learning_style[i] in reading/writing: 
    reading/writing_score_1 += 1
  if current_learning_style[i] in kinesthetic: 
    kinesthetic_score_1 += 1
visual_score = visual_score_1/3
auditory_score = auditory_score_1/4
reading/writing_score = reading/writing_score_1/2
kinesthetic_score = kinesthetic_score_1/2
print("Your visual_score is: " visual_score)
print("Your auditory_score is: " auditory_score)
print("Your reading/writing_score is: " reading/writing_score)
print("Your kinesthetic_score is: " kinesthetic_score)
array_of_scores = [(visual_score, "visual"), (auditory_score, "auditory"), (reading/writing_score, "reading/writing"), (kinesthetic_score, "kinesthetic")]
array_of_scores.sort(reverse = True)
print(array_of_scores[0][0], array_of_scores[0][1])
print(array_of_scores[1][0], array_of_scores[1][1])
final = [array_of_scores[0][1], array_of_scores[1][1]]
for i in len(2): 
  if final[i] == 'visual': 
    print("You are a visual learner. Your recommended study methods are: watching videos, mindmaps and flashcards.")
  if final[i] == 'auditory': 
    print("You are an auditory learner. Your recommended study methods are: listening to videos and listening to podcasts.")
  if final[i] == 'reading/writing': 
    print("You are an reading/writing learner. Your recommended study methods is: practicing answering techniques.")
  if final[i] == 'kinesthetic': 
    print("You are a kinesthetic learner. Your recommended study methods are: watching visual simulations and hands-on-experiments")
