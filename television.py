class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize a new Television object.

        Sets initial values for mute status, volume, power status, and channel.
        """
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of the television.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television.

        Only allows mute when the television is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increases the channel number by one.

        Only works when the television is on. Wraps around to the minimum channel when reaching the maximum.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the channel number by one.

        Only works when the television is on. Wraps around to the maximum channel when reaching the minimum.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the volume by one.

        Only works if the TV is on. Unmutes the TV if it's muted.
        Does not increase beyond MAX_VOLUME.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by one.

        Only works if the TV is on. Unmutes the TV if it's muted.
        Does not decrease below MIN_VOLUME.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Returns a string representation of the television status.

        :return: The television status.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
