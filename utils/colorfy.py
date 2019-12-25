class Colors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def header(self, string):
        """
        Returns a header type string
        :param string: gets a string
        :return: an edited string
        """
        return self.HEADER + string + self.ENDC

    def debug(self, string):
        """
        Returns a green color process string for debug workflow
        :param string: gets a string
        :return: an edited string
        """
        return self.OKGREEN + string + self.ENDC

    def info(self, string):
        """
        Returns a blue color information string for notification workflow
        :param string: gets a string
        :return: an edited string
        """
        return self.OKBLUE + string + self.ENDC

    def warn(self, string):
        """
        Returns a yellow color warning string for heads-up workflow
        :param string: gets a string
        :return: an edited string
        """
        return self.WARNING + string + self.ENDC

    def error(self, string):
        """
        Returns a red color error string for critical status workflow
        :param string: gets a string
        :return: an edited string
        """
        return self.FAIL + string + self.ENDC

    def bold(self, string):
        """
        Returns a bold type string
        :param string: gets a string
        :return: an edited string
        """
        return self.BOLD + string + self.ENDC

    def underline(self, string):
        """
        Returns a underlined type string
        :param string: gets a string
        :return: an edited string
        """
        return self.UNDERLINE + string + self.ENDC
