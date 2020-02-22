def numUniqueEmails(self, emails):
        addr_set = set()
        for email in emails:
            name, domain = email.split( "@" )
            plus_idx = name.find( "+" )
            if plus_idx != -1:
                name= name[ :plus_idx ]
            name = "".join( name.split( "." ) )
            addr_set.add( name + "@" + domain )
        return len( addr_set )