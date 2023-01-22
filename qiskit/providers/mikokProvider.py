from qiskit.providers.providerutils import filter_backends
from qiskit.providers.backend import BackendV2
from qiskit.transpiler import Target
from qiskit.providers.models import BackendConfiguration
from qiskit.providers.provider import ProviderV1
from MikokBackend import MikokBackend




class BackendService():
    """A service class that allows for autocompletion
    of backends from provider.
    """

    def __init__(self, backends):
        """Initialize service
        Parameters:
            backends (list): List of backend instances.
        """
        self._backends = backends
        for backend in backends:
            setattr(self, backend.name, backend)

    def __call__(self, name=None, filters=None, **kwargs):
        """A listing of all backends from this provider.
        Parameters:
            name (str): The name of a given backend.
            filters (callable): A filter function.
        Returns:
            list: A list of backends, if any.
        """
        # pylint: disable=arguments-differ
        backends = self._backends
        if name:
            backends = [
                backend for backend in backends if backend.name == name]

        return filter_backends(backends, filters=filters, **kwargs)


class MikokProvider(ProviderV1):

    def __init__(self):
        super().__init__()
        self.name = 'mikok_provider'
        self.backends = BackendService([MikokBackend(provider=self)]) 

    def __str__(self) -> str:
        return "Privider name = {}".format(self.name)


    
    def backends(self, name=None,filters=None, **kwargs):
        """Return a list of backends matching the specified filtering.

        Args:
            name (str): name of the backend.
            **kwargs: dict used for filtering.

        Returns:
            list[Backend]: a list of Backends that match the filtering
                criteria.
        """
        pass  




p = MikokProvider()
print(p.__str__())
print(p.__repr__())
print(p.get_backend('mikok_simulator'),[])
backend = p.get_backend('mikok_simulator')
print(backend.run('').result())