from base import Base

from requests import Response
from juju_rs.exceptions import ProviderAPIError


class ExcceptionTests(Base):

    def test_api_error(self):
        r = Response()
        r.status_code = '400'
        error = ProviderAPIError(r, "bad stuff happened")
        self.assertEqual(
            str(error),
            ("<ProviderAPIError message:bad stuff happened"
             " response:'400'>"))
