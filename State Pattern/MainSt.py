from Button import Button
from ReadyState import ReadyState 
from LockedState import LockedState


def main():
    button = Button()
    button.off()  # Output: El botón está apagado
    button.locked()  # No hay output ya que el botón está apagado
    button.ready()  # No hay output ya que el botón está apagado

    button.change_state(LockedState(button))
    button.off()  # Output: No hay output ya que el botón está bloqueado
    button.locked()  # Output: El botón está bloqueado
    button.ready()  # No hay output ya que el botón está bloqueado

    button.change_state(ReadyState(button))
    button.off()  # No hay output ya que el botón está listo
    button.locked()  # No hay output ya que el botón está listo
    button.ready()  # Output: El botón está listo

if __name__ == "__main__":
    main()