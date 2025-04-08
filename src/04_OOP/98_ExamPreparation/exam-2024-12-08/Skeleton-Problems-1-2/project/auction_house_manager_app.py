from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_ARTIFACTS = ["RenaissanceArtifact", "ContemporaryArtifact"]
    VALID_COLLECTORS = ["Museum", "PrivateCollector"]

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.VALID_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

        if any(a.name == artifact_name for a in self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")

        artifact_class = RenaissanceArtifact if artifact_type == self.VALID_ARTIFACTS[0] else ContemporaryArtifact
        self.artifacts.append(artifact_class(artifact_name, artifact_price, artifact_space))
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."


    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_COLLECTORS:
            raise ValueError("Unknown collector type!")

        if any(c.name == collector_name for c in self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")

        collector_class = Museum if collector_type == self.VALID_COLLECTORS[0] else PrivateCollector
        self.collectors.append(collector_class(collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."


    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = next((c for c in self.collectors if c.name == collector_name), None)
        if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."


    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact is None:
            return f"No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"


    def fundraising_campaigns(self, max_money: float):
        collectors = [c for c in self.collectors if c.available_money <= max_money]
        for c in collectors:
            c.increase_money()

        return f"{len(collectors)} collector/s increased their available money."


    def get_auction_report(self):
        result = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {sum(len(c.purchased_artifacts) for c in self.collectors)}",
            f"Available artifacts for sale: {len(self.artifacts)}",
            "***"
        ]

        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))
        for sc in sorted_collectors:
            result.append(f"{sc.__str__()}")

        return '\n'.join(result)