class Superhero:
    def __init__(self, name, alias, power, weakness):
        self.name = name
        self.alias = alias
        self._power = power  # Protected attribute
        self.__weakness = weakness  # Private attribute

    def reveal_identity(self):
        return f"My name is {self.name}, but the world knows me as {self.alias}!"

    def use_power(self):
        return f"{self.alias} uses {self._power}!"

    def reveal_weakness(self):
        return f"Every hero has a weakness. Mine is {self.__weakness}."

    # Method to update the private attribute (__weakness)
    def set_weakness(self, new_weakness):
        self.__weakness = new_weakness


# Subclass for a specific type of hero
class TechSuperhero(Superhero):
    def __init__(self, name, alias, power, weakness, gadget):
        super().__init__(name, alias, power, weakness)
        self.gadget = gadget

    def use_gadget(self):
        return f"{self.alias} deploys their signature gadget: {self.gadget}!"

    # Override use_power method to show polymorphism
    def use_power(self):
        return f"{self.alias} integrates technology and {self._power} to save the day!"


# Subclass for a different type of hero
class MysticSuperhero(Superhero):
    def __init__(self, name, alias, power, weakness, spellbook):
        super().__init__(name, alias, power, weakness)
        self.spellbook = spellbook

    def cast_spell(self, spell):
        return f"{self.alias} casts a powerful {spell} spell from the {self.spellbook}!"

    # Override use_power method to show polymorphism
    def use_power(self):
        return f"{self.alias} channels mystical energies and {self._power}!"


# Creating objects
iron_guardian = TechSuperhero("Alex Steel", "Iron Guardian", "super strength", "electricity", "Exo-suit")
arcane_savior = MysticSuperhero("Sophia Rune", "Arcane Savior", "arcane blasts", "physical attacks", "Grimoire of Shadows")

# Demonstrating functionality
print(iron_guardian.reveal_identity())
print(iron_guardian.use_power())
print(iron_guardian.use_gadget())
print(iron_guardian.reveal_weakness())

print("\n" + arcane_savior.reveal_identity())
print(arcane_savior.use_power())
print(arcane_savior.cast_spell("fireball"))
print(arcane_savior.reveal_weakness())
