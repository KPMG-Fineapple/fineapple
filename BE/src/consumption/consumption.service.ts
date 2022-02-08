import { Injectable, Logger } from '@nestjs/common';
import { spawn } from 'child_process';

@Injectable()
export class ConsumptionService {
  private logger = new Logger('ConsumptionService');

  getConsumption(address: string) {
    const process = spawn('python3', ['../AI/consumption-model.py']);

    process.stdout.on('data', function (data) {
      const result = JSON.parse(data.toString());
      Logger.debug('GET DATA :' + data.toString());
      return result;
    });

    process.stderr.on('data', function (data) {
      Logger.error(data.toString());
    });
  }
}
