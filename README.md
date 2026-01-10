# Jump Cat
<img width="732" height="520" alt="image" src="https://github.com/user-attachments/assets/fb8473aa-731d-4b69-8c2e-d2dfe3774bcb" />

## My solo project for the second phase of SEO FYA! 
<p>Play as a cat and jump over enemy dogs. Simplistic and fun. Targeted for a younger demographic. The game has RNG which makes it more challenging; the dogs have a different spacing each time they come back on screen, rather than the same predictable pattern. Your score increases as each bad dog goes off screen. If you bump into a dog, you lose and have to restart. Overall, I learnt a lot while working on this and PyGame is a great library. </p>



### Controls
<ul>
  <li>Game is run on Python from the game folder</li> 
  
```
python3 game.py
```
  <li>Space key to start game</li>  
  <li>Use arrow keys to move left/right and jump</li>
  <li>Double space to restart game after losing</li>
</ul>

  ### Challenges faced while developing
<ul>
  <li>
    Logic errors regarding game screen bounds (resolved by pushing the character back into bounds as soon as position reaches outside of window size)
  </li>
  <li>
      Too large hitboxes (resolved by resizing the characters)
  </li>
</ul>


