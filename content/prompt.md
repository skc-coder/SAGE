Smart Analysis & Generation for Exams. this i am builidng which uses ai to help in analyze pracite seesion, or just questions and genrate varaitons of the question and create notes of the underylying knowelge teach the question practie the varaiton for exmam goal like gate cds or learning in gneral . it keep track of question, what they are asking and notes generated. this is a This system is simply a skill for AIs to use, and I use Obsidian syntax for keeping track of the notes and questions and sources of the questions. Please be useful and create a modular, extensible, clean, small, to-the-point skill for me. Ask me questions So the notes are stored in obsidian syntax, but it is published to a static web website. Convert it to a static website using Quarto. Your job will be to, this system will be used to analyze questions or practice tests of various kinds of exams, for example, GATE exam, CDS, etc., or just any exam or question in general. Your task has is to create a well-organized notes for the questions. Your job is to keep track of the questions that I ask you about. You have to keep track of their sources. And I believe that for to prepare well for any exam, we need to do analysis of the past previous papers. So this system is mainly geared toward those those types of questions. And so user will ask the system in an AI chat environment questions and the AI should generate notes explain when AI explains the questions, the AI should store its explanation in an In an MD file for this session, later when the user is done, these files will be combined to make a good note for the subject. The practice happens with respect to a subject and possibly with respect to a topic under that subject. You have to create an index for each of the subject we discuss. The index should include topic names and under that topic name, There will be sub topic names and clicking on and under those there should be questions which through which they have been generated or related to. Clicking on any note opens the its note and and when when a user gets and for every question the AI system should generate variations of all these questions and the topic or concept been asked on by the question. With respect to the exam so that the user can learn all the things. That is that may be asked in future or what was being tested. So the user truly learns. The mistake or new concept or whatever. The user may input process the questions in various ways. One way is this will be defined in separate files. These are certain modes of using the system. In one mode, the user may give the AI system a preview of file of the test session. He has given and AI should walk through the questions one by one . the pdf will include the quesstion, wheater the user got it correct or not, 

The AI has to do these things for each question:
keep track of a datbase of the topic and exact type of thing being being asked. for example I have noticde that under mst topic gate has asked a lot of question on finding number of msts given a graph, under further clasffication the graph may be given in adjcemy matrix format or be given via certain mahtemtical condtions on edges in formulaic way. This is how you have to create a datbase of the question. You track the chatper, topic, the thing being asked, any furhter division. Of coursse if a type of question exist then ai should not add it agiain. but if a further specialization of question is asked you should add it apporitely. The databse should keep track of the question which asked that topic or type of question. Each and every question and topic and type of question should be accounted. This is a very cruical phase beacuse throuhg this the user will be able to find his weakness, find the topics which the exam is asking quesstions on and pracite more on the important topics.

THe databse should be viewable throuhg obisidan, should be powerful enough to support our needs. Recommend things that u suggest so that we can cleany achive this.

The next thng the ai has to do is to for a question that he has got write it should ask varitons on it according to the exam to test if the user truly understands the underlying concept being tested. It is import for the variation to truly test the users knoweldge. The variation should not just be the copy of the same question with different value. It should be novel, and should test the underlying or related concept. The goal is for the user to learn and to ace exam.

If the question was wrong by user then before genrating the varaitons the ai should explain the underlying concept, explain the question, wjat is being asked, give answer to the question....
if need the explation should include theorems, properitese needed. it should give intution of concepts questions the thoerems and propeitese as needed (assume the user is smart, not a baby so intution doesnt mean to reduce it to toys, u should know what i mean by intution).

Then the ai should ask varaiton on the question.

THe ai should not move on until the user says so, to next question.

THe ai has to save all the things it genertes in a folder genreted for the session. It should not worry about flow betwene the content while the session is going.

When the session is at end the user will call a /wrap cmd that should trigger the ai to make the session good and readble. 
This is a important phase. the goal here is that ai doesnt have to rewrite the whole content as this leads to token wastage, ai may miss some importnat points disuced, etc
hence in the session the thigns the ai generates should be such that later minimal changes are neeed to integrate the content in one coherant way.

Let me explain the folder structure: You may simplify t if the nested structre is too deep. Discuss it with me.
exam1/
	subject1/
		index, trakcing all the thigns in good way, easy to go through way, 
		question tracker datbase
		
		test/
		a index file for the test sessions, they simply include a link to the topics and questions dissuced in a test session
			it may support graphs for analysis, links to questions
		notes/
			topic1.md contains questions and ntoes and varaitons
			folderto orgnaize multiple related topics
		tmp/
			session1/
			conntains in session ntoes questions files
		
		
exam2/

in session the databse will be update of course...
the notes, explations questions files, variations the ai saves in tmp folder should be such that they require minimal to no changes when integrating via wrap up. OK.  WHen doing wrap move the files to notes folder, update the index, and make sure that links work.

Besides the user giving test pdf files to ai, the user may have sessions in haphzard way where he asks questions by pasting their shcressnshots or text. The ai should intellgiently suggest the subject, and exam being disscued. the ai should mainint a file for the exams the user is intereseted in. 
Again create a sessions folder for it. YOu should ask and suggest the chapters for the questions. Ofoucrse maiintin the databse.


The system should keep track of the source of the question. If it is clear for the pdf then it should automatically store and tell the user.And track the link or question number of each quetion and test. If the ai doenst find it. ask the user. The ai should infer question number from the scressnshots. if not clear ask the user eplaicitly.

AI should make a databse of questions topics subtopics etc, wrong right questions so that usser can analyze his mistake. The ai should inclue a option of /report perofracme subject/topic to analyze the perofracme of the user wrt to the subject.topic  and a /analyze subject/topic/exam to analyze the thing the exam is asking, important topcis the msot important topics...sugessitng areas to pracite more, asking to genrate varaitons, etc....

Ensure good math rendering, clear formating, readibility, etc. 

User will use the system to pracite and anlyze exam and will be a critical tool in his her success of getting top rank in the exam. 

Create a formating guidline for the way the content genrated by the ai should be. 