from pygopherd.protocols import rfc1436


class EnhancedGopherProtocol(rfc1436.GopherProtocol):
    def renderobjinfo(self, entry):
        return (
            entry.gettype()
            + entry.getname()
            + "\t"
            + entry.getselector()
            + "\t"
            + entry.gethost(default=self.server.server_name)
            + "\t"
            + str(entry.getport(default=self.server.server_port))
            + "\t"
            + str(entry.getsize())
            + "\t"
            + entry.getmimetype()
            + "\t"
            + entry.getencoding()
            + "\t"
            + entry.getlanguage()
        )
