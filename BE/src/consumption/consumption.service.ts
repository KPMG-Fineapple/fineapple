import { Injectable, Logger } from '@nestjs/common';
import { spawnSync } from 'child_process';

@Injectable()
export class ConsumptionService {
  private logger = new Logger('ConsumptionService');

  async getConsumption(address: string) {
    const process = spawnSync('python3', ['../AI/consumption-main.py']);
    const str = Buffer.from(process.stdout.toJSON().data).toString();
    const result = JSON.parse(str.substring(70, str.length));
    return result;
  }
}
