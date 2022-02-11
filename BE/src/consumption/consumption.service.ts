import { Injectable, Logger } from '@nestjs/common';
import { spawnSync } from 'child_process';

@Injectable()
export class ConsumptionService {
  private logger = new Logger('ConsumptionService');

  async getConsumption(address: string) {
    const process = spawnSync('python3', ['../AI/consumption-model.py']);
    const result = JSON.parse(
      Buffer.from(process.stdout.toJSON().data).toString(),
    );
    return result;
  }
}
