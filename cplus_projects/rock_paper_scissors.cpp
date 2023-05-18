#include <iostream>
using namespace std;

bool is_win(string user, string computer)
{
    if ((user == "r" && computer == "s") || (user == "s" && computer == "p") || (user == "p" && computer == "r"))
    {
        return true;
    }
    else
    {

        return false;
    }
}
void play()
{
    string user;
    cout << "'r' for rock, 'p', for paper, 's' for scissors";
    cin >> user;
    string rps[] = {"r", "p", "s"};
    string computer = rps[rand() % 3];

    if (user == computer)
    {
        cout << "it's a tie";
    }
    else if (is_win(user, computer))
    {
        cout << "you won";
    }
    else
    {
        cout << "computer won";
    }
}

int main()
{
    play();

    return 0;
}
