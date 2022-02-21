import { Injectable, Logger } from '@nestjs/common';
import { spawnSync } from 'child_process';

@Injectable()
export class PowerGenerationService {
  private logger = new Logger('PowerGenerationService');

  getPowerGeneration() {
    const process = spawnSync('python3', ['../AI/power-generation-main.py']);
    const str = Buffer.from(process.stdout.toJSON().data).toString();
    this.logger.debug(str.substring(22, str.length));
    const result = JSON.parse(str.substring(22, str.length));
    return result;
  }
}
