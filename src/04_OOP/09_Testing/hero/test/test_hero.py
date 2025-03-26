from unittest import TestCase
from project.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('OurHero', 5, 100.0, 20.0)
        self.enemy_hero = Hero('EnemyHero', 5, 100.0, 20.0)

    def test_hero_init(self):
        self.assertEqual('OurHero', self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(20.0, self.hero.damage)

    def test_hero_battle_equal_usernames_raises(self):
        self.enemy_hero.username = "OurHero"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_battle_health_is_smaller_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
            self.hero.health = -1
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero_battle_enemy_health_is_smaller_or_equal_to_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
            self.enemy_hero.health = -1
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight EnemyHero. He needs to rest", str(ex.exception))

    def test_hero_battle_draw_zero_health(self):
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(100.0, self.enemy_hero.health)
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)
        self.assertEqual(0.0, self.hero.health)
        self.assertEqual(0.0, self.enemy_hero.health)

    def test_hero_battle_draw_negative_health(self):
        self.hero.health = 80
        self.enemy_hero.health = 70
        self.assertEqual(80.0, self.hero.health)
        self.assertEqual(70.0, self.enemy_hero.health)
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", result)
        self.assertEqual(-20.0, self.hero.health)
        self.assertEqual(-30.0, self.enemy_hero.health)

    def test_hero_battle_win(self):
        self.enemy_hero.health = 70
        self.enemy_hero.damage = 10
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(20.0, self.hero.damage)
        self.assertEqual(70.0, self.enemy_hero.health)
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(55.0, self.hero.health)
        self.assertEqual(25.0, self.hero.damage)

    def test_hero_battle_lose(self):
        self.hero.health = 70
        self.hero.damage = 10
        self.assertEqual(70.0, self.hero.health)
        self.assertEqual(100.0, self.enemy_hero.health)
        self.assertEqual(5, self.enemy_hero.level)
        self.assertEqual(20.0, self.enemy_hero.damage)
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(6, self.enemy_hero.level)
        self.assertEqual(55.0, self.enemy_hero.health)
        self.assertEqual(25.0, self.enemy_hero.damage)

    def test_hero_str(self):
        self.assertEqual("Hero OurHero: 5 lvl\nHealth: 100.0\nDamage: 20.0\n", self.hero.__str__())






