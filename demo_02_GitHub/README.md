
# GitHub Desktop

<img src="Images/Octocat.png" width="500"/>

GitHub is an online repository for storing software. 
It is a safe location the saves successive versions of your code
so that past versions of your code can be recovered,
should you need to make corrections or replace your computer.
This is why it is called *version control software*. 
It is also useful to collaborate on software because multiple
software developers will be able to modify the same online repository.

The repository for this course can be viewed in a browser. 

<img src="Images/GitHubBeforeRefresh.png" width="500"/>


## How to Update your Repo

To complete and submit your assignments, you will want to 
```commit``` and ```push``` changes to the repository, 
after making those changes in the corresponding files 
on your local computer.

### Open GitHub Desktop

GitHub Desktop software allows you to manage changes. 
Open this programm ...

<img src="Images/GitHubOpen.png" width="500"/>

... and you should see a screen matching the examples below.
You will have to enter your GitHub login credentials
and approve your own access to the site through this particular computer. 


### Cloning a Repository

Once GitHub is open, the first step is *cloning* your repository. 
This makes a copy of the online repository and places it 
in a folder on your computer. 
Click on ```File -> Clone repository...```.

<img src="GitHubClone1.png" width="500"/>

select the repository you wish to clone.

<img src="GitHubClone2.png" width="500"/>

Then press ```Clone```.

<img src="GitHubClone3.png" width="500"/>

Now you should have a local copy of the repository
on the file system on your computer. 
It will be stored in a folder with the same name as the 
repository, e.g. ```ECP3004S21```, in a folder called ```GitHub```.

### Making Changes

Making changes is fairly straightforward. 
You simply create or delete files or make changes to them, 
within the local folder. 
Basically, you do the work you set out to do, 
as is there were no repository. 
That's the beauty of GitHub: you just do your work
and your work gets archived periodically with a few clicks 
of a button. 

In this example, I have added a file. 
As an example, it is an image of the course banner
"Python for Business Analytics".

<img src="GitHubChange1.png" width="500"/>

Following a requirement for Assignment 1, 
I rename it to a specific filename so that it will be displayed 
on the screen in the folder ```assignment_01```. 

<img src="GitHubChange2.png" width="500"/>

You should now see a description of the changes made, 
including an image, in this case. 

### Committing Your Changes

The next step is to ```commit``` your changes. 
This collects any changes that you have made into a 
package of changes. 
Typically, you will collect similar changes in one commit, 
e.g. solution to Assignment 1, Question 1. 
You type a description of the changes to inform other users, 
which could include *future you*, 
about the nature of the changes and the problem solved. 

<img src="GitHubCommit.png" width="500"/>

After the changes are committed, you can push this bundle of 
changes to your online repository. 

<img src="GitHubPush.png" width="500"/>

After the changes are pushed, your local repository, 
on your computer, should have the same contents as the remote
repository, the version online. 

<img src="GitHubPushed.png" width="500"/>


### Verifying the Changes

It is often a good idea to verify that the changes have been made
according to your expectations. 
Open your browser to the repository on ```github.com``` 
to see the folder you updated. 

<img src="Images/GitHubBeforeRefresh.png" width="500"/>

If you are already on that Webpage, you will need to refresh the Webpage. 
You should now see that the change has been made. 
In this case, we have uploaded an image;
in Assignment 1, 
you will upload images of the states of the Rodrego program
to document the operation of the register machine. 

<img src="Images/GitHubAfterRefresh.png" width="500"/>


If you notice you have made an error, simply make the change
on your local computer and ```commit``` and ```push``` again. 
Most of the work in computer programming is about
making, detecting, and correcting errors, and GitHub is a useful
tool designed to keep track of all your changes over time. 
