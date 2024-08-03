function radar_gui
    % Create the main figure
    Fig = figure('Name', 'Radar Data Visualization', 'Position', [100, 100, 600, 400]);

    % Create a polaraxes object for plotting
    PolarAxes = polaraxes('Parent', Fig, 'Position', [.1 .3 .8 .6]);

    % Create a button to update the plot
    uicontrol('Style', 'pushbutton', 'String', 'Update Plot', 'Position', [250, 50, 100, 40], 'Callback', @update_plot);

    function update_plot(~, ~)
        % Generate sample radar data
        angles = linspace(0, 2 * pi, 100);
        radii = abs(sin(angles));

        % Clear the previous plot
        cla(PolarAxes);

        % Plot new data
        polarplot(PolarAxes, angles, radii, 'LineWidth', 2);
        title(PolarAxes, 'Radar Data Visualization');
    end
end
