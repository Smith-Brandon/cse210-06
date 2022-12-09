# Earth Defender

Earth Defender is a game in which the player controls a spaceship at the bottom of the screen and must defend the Earth from asteroids. The player can move the spaceship left and right and shoot at the asteroids. Each time an asteroid hits the Earth, the player loses a life. The game ends when the player loses all of their lives. When all the asteroids on the screen are destroyed, the player advances to the next level. With each level, the asteroids move faster and there are more of them.

## Getting Started

---

Make sure you have Python 3.8.0 or newer installed on your computer. You can download it [here](https://www.python.org/downloads/). Raylib Python CFFI 3.7 or newer is also needed. This can be installed by opening a terminal and running the following command:
`python3 -m pip install raylib`

After you have installed the required dependencies, you can run the game by opening a terminal and running the following command:
`python3 earth_defender`

You can also run the program from an IDE such as PyCharm or VS Code. Start your IDE and open the earth_defender folder. Then, run the main.py file.

## Project Structure

---

The project is structured as follows:

```
root                                (The root folder for the project)
+-- earth_defender                  (source code for the game)
  +-- casting                       (The folder for the casting classes)
    +-- actor.py                    (actor class and methods)
    +-- bullet.py                   (bullet class and methods)
    +-- cast.py                     (cast class and methods)
    +-- level.py                    (level class and methods)
    +-- life.py                     (life class and methods)
    +-- objects.py                  (objects class and methods)
  +-- directing                     (The folder for the directing classes)
    +-- director.py                 (director class and methods)
  +-- services                      (The folder for the services)
    +-- keyboard_service.py         (keyboard service class and methods)
    +-- video_service.py            (video service class and methods)
  +-- shared                        (The folder for the shared classes)
    +-- color.py                    (color class and methods)
    +-- point.py                    (point class and methods)
+-- main.py                         (entry point for the game)
+-- constants.py                    (constants used throughout the program)
+-- README.md                       (general info)
```

## Required Technologies

---

- Python 3.8.0 or newer
- Raylib Python CFFI 3.7 or newer

## Controls

---

Player uses arrows to move left and right and spacebar to shoot.
Bullets that hit asteroids will destroy the asteroid.

## Authors

---

<table>
  <tr>
    <th>Name</th>
    <th>Assignments</th>
  </tr>
  <tr>
    <td>Brandon Smith</td>
    <td>Asteroid Class (Delete asteroid when hit by bullet, initialize asteroids, control fall speed, etc.)</td>
  </tr>
  <tr>
    <td>McKay Thomas</td>
    <td>Life Class (3 lives to start, subtract life when asteroids hit, end game when lives hit 0, add 1 life per 5 levels, etc.)</td>
  </tr>
  <tr>
    <td>Garret Cooper</td>
    <td>Bullet Class (Bullets shoot with space bar, collision logic, travel along y axis, etc.)</td>
  </tr>
  <tr>
    <td>Zak Sattler</td>
    <td>Constants Folder (Compile constants for directo and main, verify correct import into other classes, etc.)</td>
  </tr>
  <tr>
    <td>Kylar Sorensen</td>
    <td>Game Reset/Next Level (reset game when asteroids are destroyed, keep track of levels, increase fall speed, etc.)</td>
  </tr>
</table>

For more detailed information regarding contributions, refer to commits on GitHub.
