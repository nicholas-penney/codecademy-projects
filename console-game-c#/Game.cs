using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(String key, out int x, out int y)
    {
      y = x = 0;
      Console.WriteLine(key);
        switch(key)
        {
          case "S":
            case "DownArrow": y++; break;
          case "W":
            case "UpArrow": y--; break;
          case "D":
            case "RightArrow": x++; break;
          case "A":
            case "LeftArrow": x--; break;
        }
    }

    public new static char UpdateCursor(string key)
    {
      switch(key)
      {
        case "A":
            case "LeftArrow": return '<'; break;
        case "D":
            case "RightArrow": return '>'; break;
        case "W":
            case "UpArrow": return '^'; break;
        case "S":
            case "DownArrow": return 'v'; break;
      }
      return '.';
    }

    public new static int KeepInBounds(int coord, int max)
    {
      if (coord < 0)
      {
        return max-1;
      }
      else if (coord >= max)
      {
        return 0;
      } 
      else 
      {
        return coord;
      }
    }

    public new static bool DidScore(int xChar, int yChar, int xFruit, int yFruit)
    {
      if (xChar == xFruit && yChar == yFruit)
      {
        return true;
      } 
      else 
      {
        return false;
      }
    }
    
  }
}