# combat module
import characters
import player_character


def combat(player_character, enemy_character):
    now_moving = ""
    if player_character["current_speed"] > enemy_character["current_speed"]:
        now_moving = "player"
    else:
        now_moving = "enemy"
    while enemy_character["current_hp"] >= 0 and player_character["current_hp"] >= 0:


        if now_moving == "player":
            enemy_character["current_hp"] = enemy_character["current_hp"] - player_character["current_attack"]
            # print(player_character["current_hp"])
            # print(enemy_character["current_hp"])
            now_moving = "enemy"

        elif now_moving == "enemy":
            player_character["current_hp"] = player_character["current_hp"] - enemy_character["current_attack"]
            # print(player_character["current_hp"])
            # print(enemy_character["current_hp"])
            now_moving = "player"

    if enemy_character["current_hp"] <= 0:
        print("ENEMY IS DEAD")
        print("Your remaining hp:", end=" ")
        print(player_character["current_hp"])

    if player_character["current_hp"] <= 0:
        print("YOU DIED")
        quit()


if __name__ == '__main__':
    combat(player_character.player_character, characters.characters['ghost'])