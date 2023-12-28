from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

class MyPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        pipeline =  CodePipeline(self, "Pipeline", 
                    pipeline_name="my-pipelineGrg", 
                    synth=ShellStep("Synth",
                        input=CodePipelineSource.connection("gregonometry/my-pipeline", "main", connection_arn="arn:aws:codestar-connections:us-east-1:707231838635:connection/5b977032-777d-4ec9-82d2-c1fdf140c1a1"),
                        commands=["npm install -g aws-cdk", "python -m pip install -r requirements.txt", "cdk synth"]
                    )
                )

        # example resource
        # queue = sqs.Queue( 
        #     self, "MyPipelineQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
